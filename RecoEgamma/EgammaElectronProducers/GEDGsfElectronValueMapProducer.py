import FWCore.ParameterSet.Config as cms

def GEDGsfElectronValueMapProducer(*args, **kwargs):
  mod = cms.EDProducer('GEDGsfElectronValueMapProducer',
    gedGsfElectrons = cms.InputTag('gedGsfElectronsTmp'),
    egmPFCandidatesTag = cms.InputTag('particleFlowEGamma'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
