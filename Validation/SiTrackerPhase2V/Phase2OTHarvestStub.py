import FWCore.ParameterSet.Config as cms

def Phase2OTHarvestStub(*args, **kwargs):
  mod = cms.EDProducer('Phase2OTHarvestStub',
    TopFolderName = cms.string('TrackerPhase2OTStubV'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
