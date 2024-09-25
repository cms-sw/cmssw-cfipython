import FWCore.ParameterSet.Config as cms

def HcalTopologyIdealEP(*args, **kwargs):
  mod = cms.ESProducer('HcalTopologyIdealEP',
    Exclude = cms.untracked.string(''),
    MergePosition = cms.untracked.bool(False),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
