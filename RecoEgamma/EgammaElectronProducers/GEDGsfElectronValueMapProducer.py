import FWCore.ParameterSet.Config as cms

def GEDGsfElectronValueMapProducer(**kwargs):
  mod = cms.EDProducer('GEDGsfElectronValueMapProducer',
    gedGsfElectrons = cms.InputTag('gedGsfElectronsTmp'),
    egmPFCandidatesTag = cms.InputTag('particleFlowEGamma'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
