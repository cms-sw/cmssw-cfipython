import FWCore.ParameterSet.Config as cms

def EcalPreshowerMonitorClient(**kwargs):
  mod = cms.EDProducer('EcalPreshowerMonitorClient',
    enabledClients = cms.untracked.vstring(
      'Integrity',
      'Pedestal',
      'Summary'
    ),
    LookupTable = cms.required.untracked.FileInPath,
    prefixME = cms.untracked.string('EcalPreshower'),
    fitPedestal = cms.untracked.bool(True),
    cloneME = cms.untracked.bool(True),
    verbose = cms.untracked.bool(False),
    debug = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
