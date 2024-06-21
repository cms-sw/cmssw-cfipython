import FWCore.ParameterSet.Config as cms

def ElectronSeedMerger(**kwargs):
  mod = cms.EDProducer('ElectronSeedMerger',
    EcalBasedSeeds = cms.InputTag('ecalDrivenElectronSeeds'),
    TkBasedSeeds = cms.InputTag('trackerDrivenElectronSeeds', 'SeedsForGsf'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
