import FWCore.ParameterSet.Config as cms

def EgammaHLTPixelMatchElectronProducers(*args, **kwargs):
  mod = cms.EDProducer('EgammaHLTPixelMatchElectronProducers',
    TrackProducer = cms.InputTag('hltEleAnyWP80CleanMergedTracks'),
    GsfTrackProducer = cms.InputTag(''),
    UseGsfTracks = cms.bool(False),
    BSProducer = cms.InputTag('hltOnlineBeamSpot'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
