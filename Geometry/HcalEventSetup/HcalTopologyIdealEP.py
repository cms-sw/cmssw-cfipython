import FWCore.ParameterSet.Config as cms

def HcalTopologyIdealEP(**kwargs):
  mod = cms.ESProducer('HcalTopologyIdealEP',
    Exclude = cms.untracked.string(''),
    MergePosition = cms.untracked.bool(False),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
