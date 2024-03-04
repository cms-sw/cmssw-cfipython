import FWCore.ParameterSet.Config as cms

def SiStripLorentzAngleRunInfoTableProducer(**kwargs):
  mod = cms.EDProducer('SiStripLorentzAngleRunInfoTableProducer',
    name = cms.string('Det'),
    magFieldName = cms.string('magField'),
    doc = cms.string('Run info for the Lorentz angle measurement'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
