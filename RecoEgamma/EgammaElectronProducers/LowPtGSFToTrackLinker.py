import FWCore.ParameterSet.Config as cms

def LowPtGSFToTrackLinker(**kwargs):
  mod = cms.EDProducer('LowPtGSFToTrackLinker',
    tracks = cms.InputTag('generalTracks'),
    gsfPreID = cms.InputTag('lowPtGsfElectronSeeds'),
    gsfTracks = cms.InputTag('lowPtGsfEleGsfTracks'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
