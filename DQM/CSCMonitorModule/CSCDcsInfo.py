import FWCore.ParameterSet.Config as cms

def CSCDcsInfo(**kwargs):
  mod = cms.EDProducer('CSCDcsInfo',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
