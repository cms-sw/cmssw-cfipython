import FWCore.ParameterSet.Config as cms

def MtdEleIsoHarvester(**kwargs):
  mod = cms.EDProducer('MtdEleIsoHarvester',
    folder = cms.string('MTD/ElectronIso/'),
    option_plots = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
