import FWCore.ParameterSet.Config as cms

def TruthGraphPresetExamples(*args, **kwargs):
  mod = cms.EDAnalyzer('TruthGraphPresetExamples',
    src = cms.InputTag('truthLogicalGraphProducer'),
    presets = cms.vstring(
      'diboson',
      'full',
      'ggf',
      'gun',
      'heavyflavor',
      'resonance',
      'singletop',
      'top',
      'vbf',
      'vh'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
