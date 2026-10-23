import FWCore.ParameterSet.Config as cms

def MuGEML1FETableProducer(*args, **kwargs):
  mod = cms.EDProducer('MuGEML1FETableProducer',
    name = cms.string('l1aHistory'),
    src = cms.InputTag('tcdsDigis', 'tcdsRecord'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
