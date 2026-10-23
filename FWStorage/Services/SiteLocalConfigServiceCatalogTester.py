import FWCore.ParameterSet.Config as cms

def SiteLocalConfigServiceCatalogTester(*args, **kwargs):
  mod = cms.EDAnalyzer('SiteLocalConfigServiceCatalogTester',
    files = cms.untracked.VPSet(
      template = cms.PSetTemplate(
        file = cms.required.untracked.string,
        catalogIndex = cms.required.untracked.uint32,
        expectResult = cms.required.untracked.string
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
