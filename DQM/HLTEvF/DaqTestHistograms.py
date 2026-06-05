import FWCore.ParameterSet.Config as cms

def DaqTestHistograms(*args, **kwargs):
  mod = cms.EDProducer('DaqTestHistograms',
    dqmPath = cms.untracked.string('DAQTEST/Test'),
    lumisectionRange = cms.untracked.uint32(25),
    numberOfHistograms = cms.untracked.uint32(10),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
