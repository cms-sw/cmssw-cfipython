import FWCore.ParameterSet.Config as cms

def EcalDrivenElectronSeedColMerger(*args, **kwargs):
  mod = cms.EDProducer('EcalDrivenElectronSeedColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
