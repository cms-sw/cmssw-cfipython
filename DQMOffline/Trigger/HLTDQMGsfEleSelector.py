import FWCore.ParameterSet.Config as cms

def HLTDQMGsfEleSelector(**kwargs):
  mod = cms.EDProducer('HLTDQMGsfEleSelector',
    objs = cms.InputTag(''),
    selection = cms.string('et > 5'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
