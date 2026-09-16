import FWCore.ParameterSet.Config as cms

def HLTP2GTFilterTestAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HLTP2GTFilterTestAnalyzer',
    triggerResults = cms.InputTag('TriggerResults', '', 'TEST'),
    referencePath = cms.string(''),
    underTestPath = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
