import FWCore.ParameterSet.Config as cms

def JetTracksAssociatorAtVertex(**kwargs):
  mod = cms.EDProducer('JetTracksAssociatorAtVertex',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
