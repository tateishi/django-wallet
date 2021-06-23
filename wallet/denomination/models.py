from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Wallet(models.Model):
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name + f'({self.owner})'


class Entry(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    date = models.DateField()
    y10k = models.IntegerField(default=0)
    y5k = models.IntegerField(default=0)
    y2k = models.IntegerField(default=0)
    y1k = models.IntegerField(default=0)
    y500 = models.IntegerField(default=0)
    y100 = models.IntegerField(default=0)
    y50 = models.IntegerField(default=0)
    y10 = models.IntegerField(default=0)
    y5 = models.IntegerField(default=0)
    y1 = models.IntegerField(default=0)

    values = (10000, 5000, 2000, 1000, 500, 100, 50, 10, 5, 1)

    def _getitem(self, n):
        return self.counts[n]

    def _setitem(self, n, x):
        if n == 0:
            self.y10k = x
        elif n == 1:
            self.y5k = x
        elif n == 2:
            self.y2k = x
        elif n == 3:
            self.y1k = x
        elif n == 4:
            self.y500 = x
        elif n == 5:
            self.y100 = x
        elif n == 6:
            self.y50 = x
        elif n == 7:
            self.y10 = x
        elif n == 8:
            self.y5 = x
        elif n == 9:
            self.y1 = x

    def __getitem__(self, n):
        return self._getitem(n)

    def __setitem__(self, n, x):
        self._setitem(n, x)

    @property
    def counts(self):
        return (self.y10k, self.y5k, self.y2k, self.y1k,
                self.y500, self.y100, self.y50, self.y10, self.y5, self.y1)

    @property
    def amount(self):
        return sum([c * v for (c, v) in zip(self.counts, self.values)])

    def __str__(self):
        return f'{self.wallet} {self.date} {self.counts} {self.amount}'
