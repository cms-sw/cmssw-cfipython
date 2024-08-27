import FWCore.ParameterSet.Config as cms

def LowPtGsfElectronCoreProducer(**kwargs):
  mod = cms.EDProducer('LowPtGsfElectronCoreProducer',
    gsfPfRecTracks = cms.InputTag('lowPtGsfElePfGsfTracks'),
    ctfTracks = cms.InputTag('generalTracks'),
    superClusters = cms.InputTag('lowPtGsfElectronSuperClusters'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
