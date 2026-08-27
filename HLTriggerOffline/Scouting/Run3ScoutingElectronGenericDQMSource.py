import FWCore.ParameterSet.Config as cms

def Run3ScoutingElectronGenericDQMSource(*args, **kwargs):
  mod = cms.EDProducer('Run3ScoutingElectronGenericDQMSource',
    src = cms.required.InputTag,
    folder = cms.required.string,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
