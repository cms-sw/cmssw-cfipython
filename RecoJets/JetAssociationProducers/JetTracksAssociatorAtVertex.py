import FWCore.ParameterSet.Config as cms

def JetTracksAssociatorAtVertex(*args, **kwargs):
  mod = cms.EDProducer('JetTracksAssociatorAtVertex',
    jets = cms.InputTag(''),
    tracks = cms.InputTag('generalTracks'),
    coneSize = cms.double(0.4),
    useAssigned = cms.bool(False),
    pvSrc = cms.InputTag('offlinePrimaryVertices'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
