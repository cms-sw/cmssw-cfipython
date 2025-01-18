import FWCore.ParameterSet.Config as cms

def ExtraFromSeeds(*args, **kwargs):
  mod = cms.EDProducer('ExtraFromSeeds',
    tracks = cms.InputTag('generalTracks'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
