import FWCore.ParameterSet.Config as cms

def EventSetupRecordDataGetter(*args, **kwargs):
  mod = cms.EDAnalyzer('EventSetupRecordDataGetter',
    verbose = cms.untracked.bool(False),
    toGet = cms.VPSet(
      template = cms.PSetTemplate(
        record = cms.required.string,
        data = cms.required.vstring
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
