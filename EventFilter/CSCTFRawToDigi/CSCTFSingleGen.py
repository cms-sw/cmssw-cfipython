import FWCore.ParameterSet.Config as cms

def CSCTFSingleGen(**kwargs):
  mod = cms.EDProducer('CSCTFSingleGen',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
