import FWCore.ParameterSet.Config as cms

from .HcalSimpleReconstructor import HcalSimpleReconstructor

hfsimplereco = HcalSimpleReconstructor(
  correctionPhaseNS = 0,
  digiLabel = ('hcalDigis'),
  tsFromDB = True,
  samplesToAdd = 2,
  Subdetector = 'HF',
  correctForTimeslew = False,
  dropZSmarkedPassed = True,
  correctForPhaseContainment = False,
  firstSample = 4
)
