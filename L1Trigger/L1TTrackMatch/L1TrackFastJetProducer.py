import FWCore.ParameterSet.Config as cms

def L1TrackFastJetProducer(*args, **kwargs):
  mod = cms.EDProducer('L1TrackFastJetProducer',
    L1TrackInputTag = cms.InputTag('l1tTrackVertexAssociationProducerForJets', 'Level1TTTracksSelectedAssociated'),
    coneSize = cms.double(0.4),
    displaced = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
