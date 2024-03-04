import FWCore.ParameterSet.Config as cms

def DQMSourceEleCalib(**kwargs):
  mod = cms.EDProducer('DQMSourceEleCalib',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
