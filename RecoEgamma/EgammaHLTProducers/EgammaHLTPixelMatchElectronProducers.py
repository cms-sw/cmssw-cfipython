import FWCore.ParameterSet.Config as cms

def EgammaHLTPixelMatchElectronProducers(**kwargs):
  mod = cms.EDProducer('EgammaHLTPixelMatchElectronProducers',
    TrackProducer = cms.InputTag('hltEleAnyWP80CleanMergedTracks'),
    GsfTrackProducer = cms.InputTag(''),
    UseGsfTracks = cms.bool(False),
    BSProducer = cms.InputTag('hltOnlineBeamSpot'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
