import FWCore.ParameterSet.Config as cms

from .HcalSimpleReconstructor import HcalSimpleReconstructor

hosimplereco = HcalSimpleReconstructor(
  correctionPhaseNS = 13,
  digiLabel = ('hcalDigis'),
  tsFromDB = True,
  samplesToAdd = 4,
  Subdetector = 'HO',
  correctForTimeslew = True,
  dropZSmarkedPassed = True,
  correctForPhaseContainment = True,
  firstSample = 4
)
