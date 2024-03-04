import FWCore.ParameterSet.Config as cms

def EtlDigiHitsValidation(**kwargs):
  mod = cms.EDProducer('EtlDigiHitsValidation',
    folder = cms.string('MTD/ETL/DigiHits'),
    inputTag = cms.InputTag('mix', 'FTLEndcap'),
    optionalPlots = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
