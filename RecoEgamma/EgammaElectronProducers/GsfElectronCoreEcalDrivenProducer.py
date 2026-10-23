import FWCore.ParameterSet.Config as cms

def GsfElectronCoreEcalDrivenProducer(*args, **kwargs):
  mod = cms.EDProducer('GsfElectronCoreEcalDrivenProducer',
    gsfPfRecTracks = cms.InputTag('pfTrackElec'),
    gsfTracks = cms.InputTag('electronGsfTracks'),
    ctfTracks = cms.InputTag('generalTracks'),
    useGsfPfRecTracks = cms.bool(True),
    hgcalOnly = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
