import FWCore.ParameterSet.Config as cms

from .HcalSimpleReconstructor import HcalSimpleReconstructor

hfsimplereco = HcalSimpleReconstructor(

  Subdetector = 'HF',
  correctForPhaseContainment = False,
  correctForTimeslew = False,
  correctionPhaseNS = 0,
  samplesToAdd = 2
)
