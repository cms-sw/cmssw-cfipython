import FWCore.ParameterSet.Config as cms

def TrackExtraRekeyer(*args, **kwargs):
  mod = cms.EDProducer('TrackExtraRekeyer',
    src = cms.InputTag('generalTracks'),
    association = cms.InputTag('muonReducedTrackExtras'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
