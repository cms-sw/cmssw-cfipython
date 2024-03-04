import FWCore.ParameterSet.Config as cms

def GsfElectronCoreEcalDrivenProducer(**kwargs):
  mod = cms.EDProducer('GsfElectronCoreEcalDrivenProducer',
    gsfPfRecTracks = cms.InputTag('pfTrackElec'),
    gsfTracks = cms.InputTag('electronGsfTracks'),
    ctfTracks = cms.InputTag('generalTracks'),
    useGsfPfRecTracks = cms.bool(True),
    hgcalOnly = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
