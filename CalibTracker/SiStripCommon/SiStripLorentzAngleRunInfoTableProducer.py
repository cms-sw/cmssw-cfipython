import FWCore.ParameterSet.Config as cms

def SiStripLorentzAngleRunInfoTableProducer(*args, **kwargs):
  mod = cms.EDProducer('SiStripLorentzAngleRunInfoTableProducer',
    name = cms.string('Det'),
    magFieldName = cms.string('magField'),
    doc = cms.string('Run info for the Lorentz angle measurement'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
