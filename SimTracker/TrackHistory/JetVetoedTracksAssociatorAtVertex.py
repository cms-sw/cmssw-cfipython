import FWCore.ParameterSet.Config as cms

def JetVetoedTracksAssociatorAtVertex(**kwargs):
  mod = cms.EDProducer('JetVetoedTracksAssociatorAtVertex',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
