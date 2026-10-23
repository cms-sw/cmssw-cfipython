import FWCore.ParameterSet.Config as cms

def HLTDQMGsfEleSelector(*args, **kwargs):
  mod = cms.EDProducer('HLTDQMGsfEleSelector',
    objs = cms.InputTag(''),
    selection = cms.string('et > 5'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
