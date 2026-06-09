import FWCore.ParameterSet.Config as cms

def HcalSimpleReconstructor(*args, **kwargs):
  mod = cms.EDProducer('HcalSimpleReconstructor',
    correctionPhaseNS = cms.double(13),
    digiLabel = cms.InputTag('hcalDigis'),
    tsFromDB = cms.bool(True),
    samplesToAdd = cms.int32(4),
    Subdetector = cms.string('HO'),
    correctForTimeslew = cms.bool(True),
    dropZSmarkedPassed = cms.bool(True),
    correctForPhaseContainment = cms.bool(True),
    firstSample = cms.int32(4),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
