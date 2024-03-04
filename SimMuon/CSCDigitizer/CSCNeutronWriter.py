import FWCore.ParameterSet.Config as cms

def CSCNeutronWriter(**kwargs):
  mod = cms.EDProducer('CSCNeutronWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
