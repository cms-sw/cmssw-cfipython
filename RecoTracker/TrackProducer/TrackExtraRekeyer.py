import FWCore.ParameterSet.Config as cms

def TrackExtraRekeyer(**kwargs):
  mod = cms.EDProducer('TrackExtraRekeyer',
    src = cms.InputTag('generalTracks'),
    association = cms.InputTag('muonReducedTrackExtras'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
