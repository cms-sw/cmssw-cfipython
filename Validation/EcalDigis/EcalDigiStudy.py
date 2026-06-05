import FWCore.ParameterSet.Config as cms

def EcalDigiStudy(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalDigiStudy',
    EBdigiCollection = cms.InputTag('simEcalDigis', 'ebDigis'),
    EEdigiCollection = cms.InputTag('simEcalDigis', 'eeDigis'),
    verbose = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
