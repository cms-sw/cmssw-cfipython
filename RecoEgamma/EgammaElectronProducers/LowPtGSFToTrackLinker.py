import FWCore.ParameterSet.Config as cms

def LowPtGSFToTrackLinker(*args, **kwargs):
  mod = cms.EDProducer('LowPtGSFToTrackLinker',
    tracks = cms.InputTag('generalTracks'),
    gsfPreID = cms.InputTag('lowPtGsfElectronSeeds'),
    gsfTracks = cms.InputTag('lowPtGsfEleGsfTracks'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
