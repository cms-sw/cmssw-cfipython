import FWCore.ParameterSet.Config as cms

def EventSetupRecordDataGetter(**kwargs):
  mod = cms.EDAnalyzer('EventSetupRecordDataGetter',
    verbose = cms.untracked.bool(False),
    toGet = cms.VPSet(
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
