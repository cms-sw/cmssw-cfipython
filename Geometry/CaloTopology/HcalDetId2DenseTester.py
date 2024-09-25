import FWCore.ParameterSet.Config as cms

def HcalDetId2DenseTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalDetId2DenseTester',
    fileName = cms.untracked.string(''),
    testCalib = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
