import FWCore.ParameterSet.Config as cms

def HcalDetId2DenseTester(**kwargs):
  mod = cms.EDAnalyzer('HcalDetId2DenseTester',
    fileName = cms.untracked.string(''),
    testCalib = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
