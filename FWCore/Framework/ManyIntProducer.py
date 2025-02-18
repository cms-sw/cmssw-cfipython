import FWCore.ParameterSet.Config as cms

def ManyIntProducer(*args, **kwargs):
  mod = cms.EDProducer('ManyIntProducer',
    ivalue = cms.required.int32,
    throw = cms.untracked.bool(False),
    values = cms.VPSet(
      template = cms.PSetTemplate(
        instance = cms.required.string,
        value = cms.required.int32,
        branchAlias = cms.string('')
      )
    ),
    transientValues = cms.VPSet(
      template = cms.PSetTemplate(
        instance = cms.required.string,
        value = cms.required.int32,
        branchAlias = cms.string('')
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
