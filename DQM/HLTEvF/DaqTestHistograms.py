import FWCore.ParameterSet.Config as cms

def DaqTestHistograms(**kwargs):
  mod = cms.EDProducer('DaqTestHistograms',
    dqmPath = cms.untracked.string('DAQTEST/Test'),
    lumisectionRange = cms.untracked.uint32(25),
    numberOfHistograms = cms.untracked.uint32(10),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
