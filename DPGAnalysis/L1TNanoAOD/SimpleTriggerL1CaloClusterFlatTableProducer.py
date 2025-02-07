import FWCore.ParameterSet.Config as cms

def SimpleTriggerL1CaloClusterFlatTableProducer(*args, **kwargs):
  mod = cms.EDProducer('SimpleTriggerL1CaloClusterFlatTableProducer',
    name = cms.required.string,
    doc = cms.string(''),
    extension = cms.bool(False),
    skipNonExistingSrc = cms.bool(False),
    src = cms.required.InputTag,
    variables = cms.PSet(
      allowAnyLabel_ = cms.required.PSetTemplate(
        expr = cms.required.string,
        doc = cms.required.string,
        lazyEval = cms.untracked.bool(False),
        type = cms.string('int')
      )
    ),
    cut = cms.string(''),
    maxLen = cms.optional.uint32,
    minBX = cms.int32(-2),
    maxBX = cms.int32(2),
    alwaysWriteBXValue = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
