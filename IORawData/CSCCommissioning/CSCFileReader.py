import FWCore.ParameterSet.Config as cms

def CSCFileReader(**kwargs):
  mod = cms.EDProducer('CSCFileReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
