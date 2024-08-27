import FWCore.ParameterSet.Config as cms

def JetTracksAssociatorAtCaloFace(**kwargs):
  mod = cms.EDProducer('JetTracksAssociatorAtCaloFace',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
