import FWCore.ParameterSet.Config as cms

def ElectronSeedMerger(*args, **kwargs):
  mod = cms.EDProducer('ElectronSeedMerger',
    EcalBasedSeeds = cms.InputTag('ecalDrivenElectronSeeds'),
    TkBasedSeeds = cms.InputTag('trackerDrivenElectronSeeds', 'SeedsForGsf'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
